
import pHash
import urllib
import urllib2
import facebook

#config

#The script doesn't deal with login. You can get a valid token from 
#https://developers.facebook.com/tools/explorer/
#MAKE SURE YOU TICK the "user_photos" PERMISSION!

FACEBOOK_OAUTH_TOKEN = "INSERT_YOUR_OAUTH_TOKEN_HERE"

#####################################################################

graph = facebook.GraphAPI(FACEBOOK_OAUTH_TOKEN)

profile = graph.request("me", {"fields":"id,name,picture"})

albums = graph.request("me/albums")

compare_photos = []
compare_hashes = []

print "Obtaining profile pictures for %s..." % (profile["name"])
for album in albums["data"]:
	if album["type"] == "profile":
		albumPhotos = graph.request("%s/photos" % (album["id"]))
		for albumPhoto in albumPhotos["data"]:
			image = albumPhoto["images"][-1]
			photoName = "compared_%s.jpg" % (albumPhoto["id"])
			urllib.urlretrieve(albumPhoto["images"][-1]["source"], photoName);
			compare_photos.append(photoName)
			compare_hashes.append(pHash.imagehash(photoName))
			print "Saved %s" % (photoName)

response = graph.request("search",{"q":profile["name"], "fields":"id,name,picture", "type":"user"})
next = response["paging"]["next"].replace("https://graph.facebook.com/v1.0/", "")
while next:
	for user in response["data"]:
		urllib.urlretrieve(user["picture"]["data"]["url"], "compared.jpg");
		compared_hash = pHash.imagehash("compared.jpg")

		for compare_hash in compare_hashes:	
			hamming_distance = pHash.hamming_distance( compare_hash, compared_hash )
			if hamming_distance < 8:
				print 'Potential scammer: http://graph.facebook.com/%s Hamming distance: %d (%08x / %08x)' % (user["id"], hamming_distance, compare_hash, compared_hash)
			else:
				print 'http://graph.facebook.com/%s Hamming distance: %d' % (user["id"], hamming_distance)

		response = graph.request(next)
	if ("next" in response["paging"].keys()):
		next = response["paging"]["next"].replace("https://graph.facebook.com/v1.0/", "")
	else:
		next = None
	
	

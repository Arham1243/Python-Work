from instagrapi import Client

# Initialize Instagrapi client
client = Client()

# Login to Instagram
client.login(username="ashnakhn_14", password="lucifer123")

# Get user details (replace 'target_username' with the username of the user you want to fetch details for)
user = client.user_info_by_username("arham.khan_18")
urls = [url for url in user.bio_links]
number = user.contact_phone_number
email = user.public_email
followers = user.follower_count
bio = user.biography
# Print user details
print(f"Links: {urls}")
print(f"Phone: {number}")
print(f"Email: {email}")
print(f"Followers: {followers}")
print(f"Bio: {bio}")

# Logout from Instagram
client.logout()

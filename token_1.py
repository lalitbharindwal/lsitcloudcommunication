from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VoiceGrant

# Your Twilio Account SID, API Key SID, and API Key Secret
account_sid = 'AC6d4a7718b9c2e2ac42bf76f1e09b2662'
api_key_sid = 'SK57049fc372dfae9f14110c6df8465303'
api_key_secret = 'jLvzvEH9hIPG4wx5WKsOv3ZqNG6lCrur'

# Create an access token
token = AccessToken(account_sid, api_key_sid, api_key_secret)

# Set the identity of the token (user)
token.identity = '+918796775539'

# Grant access to Twilio Voice
voice_grant = VoiceGrant(
    outgoing_application_sid='APb10c56d5ea10aa441f769fb4263a6ddd',
    incoming_allow=True  # Optional: allow incoming calls
)
token.add_grant(voice_grant)

# Serialize the token as a JWT and return it
print(token.to_jwt())

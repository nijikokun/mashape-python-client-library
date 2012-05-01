
import hmac
import hashlib
import base64

class AuthUtils:

	@staticmethod
	def generate_authentication_header(public_key, private_key):
		digest_maker = hmac.new(private_key, public_key, hashlib.sha1)
		hash = digest_maker.hexdigest()
		return { "Proxy-Authorization" : base64.b64encode(public_key + ":" + hash) }

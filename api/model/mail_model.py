from google.appengine.ext import ndb
from protorpc import messages

class MailModel(ndb.Model):
  author = ndb.KeyProperty(kind='PlayerModel') # Not required, so that we can send out admin mail.
  recipients = ndb.KeyProperty(kind='GuildModel', repeated=True)
  mail_content = ndb.TextProperty(required=True)
  ## Todo: consider adding a subject line

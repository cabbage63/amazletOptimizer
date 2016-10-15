from __future__ import print_function
import sys
from oauth2client import client
from googleapiclient import sample_tools

def main(argv):
  # Authenticate and construct service.
  service, flags = sample_tools.init( argv, 'blogger', 'v3', __doc__, __file__, scope='https://www.googleapis.com/auth/blogger')

  #input your blog ID
  BLOG_ID = ********************

  try:
      posts = service.posts()

      request = posts.list(blogId=BLOG_ID)
      while request != None:
        posts_doc = request.execute()
        if 'items' in posts_doc and not (posts_doc['items'] is None):
            for post in posts_doc['items']:
              print(post['title'])
              temp_body = post['content']
              temp_body = temp_body.replace('http://ecx.images-amazon.com/','https://images-fe.ssl-images-amazon.com/')
              temp_body = temp_body.replace('http://www.amazon.co.jp/','https://www.amazon.co.jp/')
              post['content'] = temp_body
              update = posts.update(blogId=BLOG_ID,postId=post['id'],body=post).execute()
        request = posts.list_next(request, posts_doc)

  except client.AccessTokenRefreshError:
      print ('The credentials have been revoked or expired, please re-run' 'the application to re-authorize')

if __name__ == '__main__':
          main(sys.argv)

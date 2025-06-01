select id
     , app
     , name
     , applied::text::date 
 from django_migrations 
LIMIT 10;
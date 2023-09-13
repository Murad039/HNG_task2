
# FLASK BASIC CRUD APP

#BASE URL : https://shakhaoat.pythonanywhere.com/api 





## INTRODUCTION 

The person webservice rest api that allows users to interact with person resource.The webservice provide basic crud operation for managing person object


## UML diagram


+----------------------+           +------------------+
|      Flask App       |      |      Person      |
|-------- -------------|      |------------------|
|                      |      | - id : Integer   |
|   POST /api          |      | - name : String  |
|   GET /<user_id>     |      +------------------+
|   PUT /<user_id>     |
|   DELETE /<user_id>  |
+----------------------+



## RESOURCE
A person object represants an individual with a name.

#fields
id : integer ,
name : string


## API END POINTS

#1.Create a person 
#Endpoint :POST/api 

#request :
{
    "name : "elon musk"
}

#response :
{
    "id"    : 1
    "name" : "elon musk"
}

#2.Retrive a person
#Endpoint GET/api/user_id 

#response :
{
    "id" : 1,
    "name" : "Elon musk"
}

#3.Update a person
#Endpoint PUT/api/user_id 

#request
{
    "name" : "name updated"
}

#response 
{
    "id" : 1
    "name": "name updated"
}

#4.DELETE a person 
#Endpoint DELETE/api/user_id

#response 
{
    "message" : "Person deleted successfully"
}


## ERROR HANDLING

1) 404 ban request 
2) 404 not found
3) 405 Method not allowed 


## Testing

extensive test was to make sure that crud operation works properly


## Testing

extensive test was to make sure that crud operation works properly


## CONCLUSION

The person webservice is a simple and easy to use interface for managing person.use provided end points to manage your person data 


## Maintainer 
muradhossain186@gmail.com 
## Maintainer 
muradhossain186@gmail.com 
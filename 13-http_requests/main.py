# Requests and JSON
# Requests is a popular library for making HTTP requests in Python.
# JSON is a popular library for working with JSON data in Python. It is by default part of the Python standard library.

# Install requests (before using it) via terminal: pip install requests

# Import the requests library
import requests
import json  

# Example 1: Simple GET Request
# =================================
# Send a GET request to the JSONPlaceholder API to retrieve a list of users
def get_posts():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Failed to retrieve posts. Status code: {response.status_code}")

# Example 2: POST Request with JSON Data
# =======================================
# Send a POST request to the JSONPlaceholder API to create a new post
def create_post(title, body, userId):
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {"title": title, "body": body, "userId": userId}
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print("Post created successfully!")
        print(response.json())
    else:
        print(f"Failed to create post. Status code: {response.status_code}")

# Example 3: PUT Request with JSON Data
# ======================================
# Send a PUT request to the JSONPlaceholder API to update a post
def update_post(postId, title, body):
    url = f"https://jsonplaceholder.typicode.com/posts/{postId}"
    data = {"title": title, "body": body}
    response = requests.put(url, json=data)
    if response.status_code == 200:
        print("Post updated successfully!")
        print(response.json())
    else:
        print(f"Failed to update post. Status code: {response.status_code}")

# Example 4: DELETE Request
# =========================
# Send a DELETE request to the JSONPlaceholder API to delete a post
def delete_post(postId):
    url = f"https://jsonplaceholder.typicode.com/posts/{postId}"
    response = requests.delete(url)
    if response.status_code == 200:
        print("Post deleted successfully!")
    else:
        print(f"Failed to delete post. Status code: {response.status_code}")

# Advanced Example: Handling JSON Data with Nested Objects
# =========================================================
# Send a GET request to the JSONPlaceholder API to retrieve a list of comments
def get_comments():
    url = "https://jsonplaceholder.typicode.com/comments"
    response = requests.get(url)
    if response.status_code == 200:
        comments = response.json()
        for comment in comments:
            print(f"Post ID: {comment['postId']}")
            print(f"Comment ID: {comment['id']}")
            print(f"Name: {comment['name']}")
            print(f"Email: {comment['email']}")
            print(f"Body: {comment['body']}\n")
    else:
        print(f"Failed to retrieve comments. Status code: {response.status_code}")

# Example of Parsing JSON Data
# ===========================================================
# Send a GET request to the JSONPlaceholder API to retrieve a comment
def fetch_and_parse_json(post_id):
    """Fetch JSON data from JSONPlaceholder API, parse it, and convert it back to an object."""
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    try:
        response = requests.get(url)                # Send GET request
        response.raise_for_status()                 # Raises an error for bad responses (4xx, 5xx)

        data = response.json()                      # Parse JSON response into a Python dictionary (object)
        print("Parsed JSON Data:")
        print(json.dumps(data, indent=4))           # Pretty print JSON

        # Convert the dictionary back to a JSON string
        json_string = json.dumps(data)              # Serialize object to a JSON formatted string
        print("\nConverted JSON to String:")
        print(json_string)

        # Convert the JSON string back to a Python object (dictionary)
        python_object = json.loads(json_string)     # Deserialize JSON formatted string to a Python object
        print("\nConverted JSON String back to Python Object:")
        print(python_object)

        # Access specific fields from the restored Python object
        print("\nTitle from restored object:", python_object['title'])
        print("Body from restored object:", python_object['body'])

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)


# Example 1 usage: Simple GET Request
# get_posts()

# Output:
# [{'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz', 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org', 'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'}}, {'id': 2, 'name': 'Ervin Howell', 'username': 'Antonette', 'email': 'Shanna@melissa.tv', 'address': {'street': 'Victor Plains', 'suite': 'Suite 879', 'city': 'Wisokyburgh', 'zipcode': '90566-7771', 'geo': {'lat': '-43.9509', 'lng': '-34.4618'}}, 'phone': '010-692-6593 x09125', 'website': 'anastasia.net', 'company': {'name': 'Deckow-Crist', 'catchPhrase': 'Proactive didactic contingency', 'bs': 'synergize scalable supply-chains'}},....]
# -----------------------------------

# Example 2 usage: POST Request with JSON Data
# create_post("My New Post", "This is my new post.", 1)

# Output:
# {'title': 'My New Post', 'body': 'This is my new post.', 'userId': 1, 'id': 101}
# -----------------------------------

# Example 3 usage: PUT Request with JSON Data
# update_post(1, "My Updated Post", "This is my updated post.")

# Output:
# {'title': 'My Updated Post', 'body': 'This is my updated post.', 'id': 1}
# -----------------------------------

# Example 4 usage: DELETE Request
# delete_post(1)

# Output:
# Post deleted successfully!
# -----------------------------------

# Advanced Example usage: Handling JSON Data with Nested Objects
# get_comments()

# Output:
# Post ID: 1
# Comment ID: 1
# Name: Leanne Graham
# Email: Sincere@april.biz
# Body: laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium....
# ...
# ...
# Post ID: 100
# Comment ID: 500
# Name: ex eaque eum natus
# Email: Emma@joanny.ca
# Body: perspiciatis quis doloremque
# veniam nisi eos velit sed
# id totam inventore voluptatem laborum et eveniet
# aut aut aut maxime quia temporibus ut omnis
# -----------------------------------

# Example of Parsing JSON Data. Call the function with a specific post ID
# fetch_and_parse_json(1)

# Output:
# Parsed JSON Data:
# {
#     "userId": 1,
#     "id": 1,
#     "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
#     "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
# }

# Converted JSON to String:
# {"userId": 1, "id": 1, "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit", "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"}

# Converted JSON String back to Python Object:
# {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}

# Title from restored object: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
# Body from restored object: quia et suscipit
# suscipit recusandae consequuntur expedita et cum
# reprehenderit molestiae ut ut quas totam
# nostrum rerum est autem sunt rem eveniet architecto
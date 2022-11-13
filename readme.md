
# Coding Challenge

Develop a Web service.
## Author

 [@abdulbaqui](https://github.com/abdulbaqui)


## Run Locally

Clone the project

```bash
  git clone https://github.com/abdulbaqui/file-handling-backend.git
```

To run this project navigate to the directory "file-handling-backend" then follow the instructions below.

### Building a virtual environment:
Creating virtual envirnment is necessary to avoid any unwanted issue that arise. More than that to avoid poluting local Python envirnment.

```bash
  Python -m venv venv
```
Here second venv is directory name where your environment would be created. You can name it what ever you want. Now you need to activate the virtual envirnment. Activating virtual envirnemnet varies the type of operating system  you are using.

Windows 
```bash
  venv\Scripts\activate
```

Linux\MacOs
```bash
  source venv/bin/activate
```
Your Output would be some what like this.
```bash
  (venv) ..\file-handling-backend\venv\Scripts>
```
Now as you have sucessfully activated your virtual environment lets move toward installing dependencies. Now run the following bash command in your activated envirnment this will install your project dependencies.

Navigate to file-handling-backend directory
```bash
  cd file-handling-backend
```
After this 
```bash
  pip install -r requirements.txt
```
This will install all the necessary required for running this project. 

## Running Application

Finally if you are well aware of Using Django framework than you don't need help from here you can skip this part. This section will include testing server and making migrations. Testing server by running requires you to navigate to the directory where your "manage.py" 
reside. After it please run the following command.

```bash
  python manage.py runserver
```
Hopefully you will get this output
```bash
Django version 4.1.3, using settings 'fhcore.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C. 
```

## API Endpoints

The task and endpoints are as follows:

### file upload

```POST::http <domain>:<port>/upload/ ```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| file    | file   | **Required**. Your files   |

#### Response
```json
"Files Uploaded!"
```
### one random line
```GET:http <domain>:<port>/upload/one_rendomline/  ```

#### Response
```json
[
    {
        "linenumber": 496,
        "filename": "xyz.json",
        "frequently_occured": "{"
    },
    {
        "linenumber": 30,
        "filename": "xyz1.txt",
        "frequently_occured": "\n"
    },
    {
        "linenumber": 34,
        "filename": "xyz2.xml",
        "frequently_occured": "e"
    }
]
```

### one random line backwards
```POST:http <domain>:<port>/upload/one_rendomline_backward/ ```
| Parameter     | Type     | Description                |
| :--------     | :------- | :------------------------- |
| line_number | string | **Required**.              |

#### Response
```json
[
    "filename:media/xyz.json, line number:10, readline:  },\n",
    "filename:media/xyz1.txt, line number:10, readline:\n",
    "filename:media/xyz2.xml, line number:10, readline:      with XML.</description>\n"
]
```

### longest 100 lines
```GET:http <domain>:<port>/upload/longest_hundred_lines/ ```

#### Response
```json
"filename:media/xyz2.xml,line:      <author>O'Brien, Tim</author>\n"
```

### 20 longest lines of one file
```GET:http <domain>:<port>/upload/twenty_longestline_onefile/ ```

#### Response
```json
[
    {
        "line": "detail, with attention to XML DOM interfaces, XSLT processing,"
    },
    {
        "line": "conference, tempers fly as feathers get ruffled.</description>"
    },
    {
        "line": "<description>Microsoft Visual Studio 7 is explored in depth,"
    },
    {
        "line": "<description>After an inadvertant trip through a Heisenberg"
    },
    {
        "line": "looking at how Visual Basic, Visual C++, C#, and ASP+ are"
    },
    {
        "line": "detail in this deep programmer's reference.</description>"
    },
    {
        "line": "<description>Microsoft's .NET initiative is explored in"
    },
    {
        "line": "<description>The Microsoft MSXML3 parser is covered in"
    },
    {
        "line": "agent known only as Oberon helps to create a new life"
    },
    {
        "line": "<title>Visual Studio 7: A Comprehensive Guide</title>"
    },
    {
        "line": "<title>Microsoft .NET: The Programming Bible</title>"
    },
    {
        "line": "society in England, the young survivors lay the"
    },
    {
        "line": "thousand leagues beneath the sea.</description>"
    },
    {
        "line": "integrated into a comprehensive development"
    },
    {
        "line": "foundation for a new society.</description>"
    },
    {
        "line": "<publish_date>2001-04-16</publish_date>"
    },
    {
        "line": "<author>Gambardella, Matthew</author>"
    },
    {
        "line": "<title>XML Developer's Guide</title>"
    },
    {
        "line": "<author>Randall, Cynthia</author>"
    },
    {
        "line": "of being quantum.</description>"
    }
]
```


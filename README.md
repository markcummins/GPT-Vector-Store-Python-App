## GPT Vector Store Python App
### Python Helpers for Syncing Multilingual Files to a Vector Store

**Step 1: create a .env folder and add the Env Variables to it.**

```
ENV_AI_ORGANIZATION=org-1234abcd
ENV_AI_API_KEY=sk-proj-1234abcd
```

**Step 2: Install the packages**

`pip install -r requirements.txt`

**Step 3: Add your files to the exports folder **

```
├── exports/my-folder/file1.txt
├── exports/my-folder/file2.txt
└── exports/my-folder/file3.txt
```

**Step 4: Run the Python3 Detector to automatically split the files into seperate folders**

- `python3 detect.py --folder ./exports/my-folder`

```
├── exports/my-folder/en/file1.txt
├── exports/my-folder/es/file2.txt
└── exports/my-folder/es/file3.txt
```

**Step 5: Create the Vector Store and get the ID of the new store**

- `python3 vector-create.py -p proj_1234 -n 'My Store Name'`

**Step 6: Upload the files to the Vector Store**

Note, this might take a bit of time to do. To do it in smaller batches, you can manually
add the files to a seperate folder and run this command on the smaller folder:

- `python3 vector-sync.py --vector_id vs_tdLzPIxWgvYIBd7Z0NR7GKW5 --folder ./exports/my-folder/en/`

**Other Commands**

List All Files Uploaded to the Vector Stores:
`python3 vector-listfiles.py`

List Local Files (Just used for testing)
`python3 listfiles.py --folder ./exports/my-folder/`


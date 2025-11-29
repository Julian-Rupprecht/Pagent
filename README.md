# Pagent


## Developement 

### UV
+ Install UV package manager for **blazingly fast** installation

    Linux/Mac

    ```pipx install uv```

    or 

    ```curl -LsSf https://astral.sh/uv/install.sh | sh```

    Windows

    ```powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"```

### Django


In the root folder of the project run
```python manage.py runserver```

### DaisyUI
1. Run the following command to install DaisyUI

    Linux/Mac

    ```cd pagent_server/static/css && curl -sL daisyui.com/fast | bash```

    Windows

    ```cd pagent_server/static/css && powershell -c "irm daisyui.com/fast.ps1 | iex"```

2. Run Tailwind CSS executable to generate output.css

    Linux/Mac

    ```pagent_server/static/css/tailwindcss -i pagent_server/static/css/input.css -o pagent_server/static/css/output.css --watch```

    Windows

    ```pagent_server/static/css\tailwindcss.exe -i pagent_server/static/css/input.css -o pagent_server/static/css/output.css --watch```


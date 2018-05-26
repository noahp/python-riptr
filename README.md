[![PyPI version](https://img.shields.io/pypi/v/riptr.svg?longCache=true&style=for-the-badge)](https://pypi.org/project/riptr/)

# riptr
Text substitution similar to `tr` or `sed s//` but without the frustration. Uses plain old python regex style.

# Installing
Now deployed to pypi, install with:
```bash
pip install riptr
```
This adds the `riptr` and `rtr` cli tools to your python environment path.

# Usage
```bash
echo "some example text 1234" > test.file

# default output is stdout
riptr -m "^(.*?)([\d]{2})" -s "\g<1>56" test.file
some example text 5634

# specify patch mode 'p'
riptr -m "^(.*?)([\d]{2})" -s "\g<1>56" -o p test.file
---
+++
@@ -1 +1 @@
-some example text 1234
+some example text 5634

# or inplace
riptr -m "^(.*?)([\d]{2})" -s "\g<1>56" -o i test.file
cat test.file
some example text 5634

```
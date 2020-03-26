# Compile SCSS

A CLI utility for compiling multiple SCSS files into a single CSS file to avoid linking a million CSS files within a project.

## Usage

Place `compile_scss.py` in the same directory as SCSS files.

Run `python compile_scss.py`

By default, a CSS file named `index.css` will be generated in the same directory as the SCSS files.

**Compile Sass** is still in development but has been tested successfully but not extensively with:

* Variables
* @import statements
* Functions (basic)
* Mixins (basic)

### Options

Currently `compile_scss.py` can be passed a variety of command line arguments to augment the output of your CSS.

* `output_dir` - Target directory for the generated CSS file. Default is `./` which is the same directory as the SCSS files.

* `output_name` - Name of the generated CSS file. Default is `index.css`

* `format` - Libsass' Sass.compile() function accepts an argument called `output_style`. This changes the formatting of the generated CSS. The following values are valid:

  * nested
  * expanded
  * compact
  * compressed

If no options are passed to `compile_scss.py`, the default values will be used.

Options are passed after the `compile_scss.py`, separated by spaces:

>`python compile_scss.py output_dir='<DIRECTORY_PATH>' output_name='<FILENAME>.css' format='<OPTION>'`

---

## Example

The following command is run in a terminal in which we've navigated to the directory containing SCSS files and `compile_scss.py`:

>`python compile_scss.py output_dir='../css/' output_name='main.css' format='compressed'`

Will collect the contents of the directory where `compile_scss.py` is located: `./`

It will then compile the SCSS it finds into a single CSS file called `main.css` which it will place in the directory named `css/` in the parent directory relative to `compile_scss.py`: `../`. The final file path of the CSS will be `../css/main.css`

The `format='compressed'` option generates a minified version of the CSS file, removing white space and putting everything on a single line.

---

At the moment, `compile_scss.py` cannot accept its other two options:

* `dir` - will allow the user to specify the directory in which the SCSS files reside, without placing `compile_scss.py` in the same directory

* `ext` - will allow the user to use the .sass extension.

Hopefully this will change in future updates, but they may be limitations within Libsass.
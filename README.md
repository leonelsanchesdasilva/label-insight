# label-insight

For this exercise, I decided to use Python because 1) I know that Label Insight uses it, and 2) it sparks joy.

## Usage

In Python REPL or in another Python source, import the files:

    >>> import missing_letters
    >>> import particles

For `missing_letters`, there's a method called `getMissingLetters` that can be used like this:

    >>> missing_letters.getMissingLetters("A quick brown fox jumps over the lazy dog")

`getMissingLetters` returns a string with all the latin alphabet letters that are not present in the phrase provided as the function parameter.

For `particles`, there's a method called `animate` that takes two parameters:

    >>> particles.animate(2, "..R....")

The first parameter is the particles speed (positive integer). The second parameter is the initial chamber state (string). `animate` returns an array with all the simulated chamber states. The last state is always an empty chamber (a string with dots only).

Some parameter validations are performed beforehand. Each validation failure will throw a `ValueError exception`.

## Testing

At the project root, run:

    $ pytest

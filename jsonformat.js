// json formatter script
// for now, to be used in tandem with Sublime Text autoformat
// (somewhat obsoleted by python -m json.tool)

var fs = require('fs');

// This code style is not at all flashy at present. That's fine.
// Could be improved by using a stack

var whitespace = [' ', '\t', '\n'];

var isWhitespace = function(char) {
    return whitespace.indexOf(char) > -1;
};

var improve = function(original) {
    var newString = '';

    var charIndex = 0;
    var prevChar;
    var curChar;
    var nextChar;

    while (charIndex < original.length) {
        curChar = original[charIndex];
        prevChar = (charIndex == 0) ? null : original[charIndex-1];
        nextChar = (charIndex+1 < original.length) ? original[charIndex+1] : null;

        if (curChar == '{' || curChar == '[') {
            // if (prevChar && !isWhitespace(prevChar)) {
            //     // if not preceded by whitespace
            //     newString += ' ';
            // }

            newString += curChar;

            // (functionize? requires access to newString...)
            if (nextChar && ! isWhitespace(nextChar)) {
                // TODO Skip trailing spaces?
                newString += '\n';
            }
        }
        else if (curChar == '}' || curChar == ']') {
            if (prevChar && !isWhitespace(prevChar)) {
                // if not preceded by whitespace
                newString += ' ';
            }

            newString += curChar;

            // THe only allowable next character is ','
            if (nextChar && nextChar != ',' && nextChar != '\n') {
                newString += '\n';
            }
        }
        else if (curChar == ',' && nextChar && nextChar != '\n') {
            newString += ',\n'
        }
        else if (prevChar && prevChar == '"' && curChar == ':' && nextChar && nextChar != ' ') {
            // (prevChar has already been added.)
            newString += ': ';
        }
        else {
            newString += curChar;
        }

        charIndex += 1;
    }

    if (original.length > newString.length) {
        console.log('warning: output somehow shorter than input.');
    }

    return newString;
};




// Check for filename parameter
if (process.argv.length < 3) {
    console.log('usage: node ' + process.argv[1] + ' filename');
    process.exit(1);
}

var filename = process.argv[2];

fs.readFile(filename, 'utf8', function(err, data) {
    if (err) {
        throw err;
    }

    var formatted = improve(data);
    console.log(formatted);
});


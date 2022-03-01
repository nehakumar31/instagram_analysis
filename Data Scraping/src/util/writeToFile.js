const fs = require('fs');
function writeToFile(dataToWrite, outputFileNameWithExtension) {
    try {
        fs.writeFile(`${outputFileNameWithExtension}`, JSON.stringify(dataToWrite), function (err) {
            if (err) throw err;
            console.log(`Data written to ${outputFileNameWithExtension}`);
        });
    } catch (error) {
        console.error(error);
    }
}

function writeTextToFile(dataToWrite, outputFileNameWithExtension) {
    try {
        fs.writeFile(`${outputFileNameWithExtension}`, dataToWrite, function (err) {
            if (err) throw err;
            console.log(`Data written to ${outputFileNameWithExtension}`);
        });
    } catch (error) {
        console.error(error);
    }
}

function writeArrayToFile(dataToWrite, outputFileNameWithExtension) {
    try {
        fs.writeFile(`${outputFileNameWithExtension}`, dataToWrite.join('\n'), function (err) {
            if (err) throw err;
            console.log(`Data written to ${outputFileNameWithExtension}`);
        });
    } catch (error) {
        console.error(error);
    }
}

function readArrayFromFile(fileName) {
    try {
        data = fs.readFileSync(fileName, {encoding:'utf8', flag:'r'})
        return data.split("\n")
    } catch (error) {
        console.error(error);
    }
}

module.exports = {
    writeToFile, writeTextToFile, writeArrayToFile, readArrayFromFile
}
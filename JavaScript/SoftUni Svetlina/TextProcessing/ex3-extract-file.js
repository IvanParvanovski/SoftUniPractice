function extractFile(filePath) {
    const regexPattern = /(?<name>[^\\]+(?:\.\w+)*)\.(?<extension>\w+)/;
    
    const res = regexPattern.exec(filePath);
    console.log(`File name: ${res.groups.name}`);
    console.log(`File extension: ${res.groups.extension}`)
}

extractFile('C:\\Internal\\training-internal\\Template.pptx');

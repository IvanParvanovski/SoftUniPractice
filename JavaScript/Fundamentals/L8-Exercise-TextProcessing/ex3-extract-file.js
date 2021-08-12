function extractFile(filePath) {
    let filePathTokens = filePath.split('\\');
    let file = filePathTokens.pop();
    let fileTokens = file.split('.');

    let fileExtension = fileTokens.pop();
    let fileName = fileTokens.join('.');
    
    console.log(`File name: ${fileName}`);
    console.log(`File extension: ${fileExtension}`);
}

extractFile('C:\\Internal\\training-internal\\Template.pptx');
extractFile('C:\\Projects\\Data-Structures\\LinkedList.cs');

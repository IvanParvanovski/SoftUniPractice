function fromJSONtoHTMLTable(input) {
    const students = JSON.parse(input);    
    let result = ['<table>\n', '\t<tr>'];

    for (const key of Object.keys(students[0])) {
        result.push(`<th>${key}</th>`);
    }

    result.push('</tr>\n');

    for (const student of students) {
        result.push('\t<tr>');
        
        for (const item of Object.entries(student)) {
            result.push(`<td>${item[1]}</td>`);
        }

        result.push('</tr>\n');
    }

    result.push('</table>')
    console.log(result.join(''));
}

fromJSONtoHTMLTable(`[{"Name":"Pesho",
"Score":4,
"Grade":8},
{"Name":"Gosho",
"Score":5,
" Grade":8},
{"Name":"Angel",
"Score":5.50,
" Grade":10}]`
)

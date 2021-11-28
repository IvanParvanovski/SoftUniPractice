export function renderTemplate(templateAsString) {
    const pattern = /{{(.+?)}}/gm;

    return (data) => {
        return templateAsString.replace(pattern, (match, propName) => {
            return data[propName]
        }); 
    }
    
}

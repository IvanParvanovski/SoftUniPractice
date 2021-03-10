// function highlight(){
//     if(this.className.includes('highlighted')){
//         this.className = this.className.replace('highlighted', '')
//     } else {
//         this.className += 'highlighted';
//     }
// }
// windom.onload = function() {
//     console.log(document.getElementsByClassName('highlightable'));
//     [...document.getElementsByClassName('highlightable')]
//         .forEach(element => {
//             console.log(element)
//             element.addEventListener('mouseenter', highlight);
//             element.addEventListener('mouseout', highlight);
//         });
// }
class Pagination {

    constructor(elements, elementsPerPage) {
        this.elements = elements;
        this.elementsPerPage = elementsPerPage;
        this.pages = [];

        this.createPages();
    }

    pageCount() {
        return this.pages.length;
    }

    itemCount() {
        return this.elements.length;
    }

    pageItemCount(index) {
        if (index < 0 || index >= this.pageCount()) {
            return -1;
        }  

        return this.pages[index].length;
    }

    pageIndex(element) {
        let currentArr = [];
        let pageIndex = 0;
        let newPageIndex = 0;

        for (let i = 0; i < this.itemCount(); i++) {
            if (i + 1 == element) {
                return newPageIndex - 1;
            }

            if (currentArr === undefined) {
                return -1;
            }

            if (newPageIndex == 0 || currentArr.length - 1 == pageIndex) {
                pageIndex = 0;
                currentArr = this.pages[newPageIndex]
                newPageIndex++;
            }

            pageIndex++;
        }

        return -1;
    }

    createPages() {
        let currentPage = [];

        for (let i = 0; i < this.elements.length; i++) {
            if (i != 0 && i % this.elementsPerPage == 0) {
                this.pages.push(currentPage);
                currentPage = [];
            }

            currentPage.push(this.elements[i]);
        }   
        
        if (currentPage.length != 0) {
            this.pages.push(currentPage);
        }
    }
}

var pagination = new Pagination(['a', 'b', 'c', 'd', 'e', 'f'], 4);
console.log(pagination.pageCount());
console.log(pagination.itemCount());
console.log(pagination.pageItemCount(0));
console.log(pagination.pageItemCount(1));
console.log(pagination.pageItemCount(2));

console.log(pagination.pageIndex(5));
console.log(pagination.pageIndex(2));
console.log(pagination.pageIndex(20));
console.log(pagination.pageIndex(-10));

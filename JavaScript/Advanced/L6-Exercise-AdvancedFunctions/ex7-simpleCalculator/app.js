function calculator() {
    const elements = {};

    function init(selector1, selector2, resultSelector) {
        elements.firstInput = document.querySelector(selector1);
        elements.secondInput = document.querySelector(selector2);
        elements.resultInput = document.querySelector(resultSelector);
    }

    function add() {
        this.resultInput.value = Number(this.firstInput.value) + 
                                 Number(this.secondInput.value);
    }

    function subtract() {
        this.resultInput.value = Number(this.firstInput.value) -
                                 Number(this.secondInput.value);
    }

    return {
        init,
        add: add.bind(elements),
        subtract: subtract.bind(elements),
    }
}

const calculate = calculator(); 
calculate.init('#num1', '#num2', '#result'); 


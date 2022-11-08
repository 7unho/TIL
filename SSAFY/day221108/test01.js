// import {title, add, sub} from './test01_module.js';
import {title, add, sub} from './test02_module.js';

new Vue({
    el: "#app",
    data: {
        num1: 0,
        num2: 0,
        op: "+",
        result: 0,
    },
    methods: {
        doCal() {
            if (this.op === '+') this.result = add(this.num1 + this.num2);
            else                 this.result = sub(this.num1 - this.num2);
        }
    },
});

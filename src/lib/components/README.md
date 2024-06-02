Here is the pattern for named parameter passing in Javascript...

```javascript
/**
 * My Function
 *
 * @param {string} arg1 Argument 1
 * @param {string} arg2 Argument 2
 */
function myFunc(arg1, arg2) { }

var arg1, arg2;
myFunc(arg1='Param1', arg2='Param2');
```
ref: https://stackoverflow.com/questions/11796093/is-there-a-way-to-provide-named-parameters-in-a-function-call-in-javascript
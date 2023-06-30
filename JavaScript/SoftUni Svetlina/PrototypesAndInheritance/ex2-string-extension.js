function solve() {
    String.prototype.ensureStart = function(str) {
        if (!this.startsWith(str)) {
            return str + this;
        }

        return this.toString();
    }

    String.prototype.ensureEnd = function(str) {
        if (!this.endsWith(str)) {
            return this + str;
        }

        return this.toString();
    }

    String.prototype.isEmpty = function() {
        return this.length === 0;
    }

    String.prototype.truncate = function(n) {
        if (n < 4) {
            return '.'.repeat(n);
        }
        if (this.length <= n) {
            return this.toString();
        }
        let lastIndex = this.substr(0, n - 2).lastIndexOf(' ');
        
        if (lastIndex != -1) {
            return this.substr(0, lastIndex) + '...';
        } else {
            return this.substr(0, n - 3) + '...';
        }    
    }

    String.prototype.format = function(string, ...params) {
        for (let i = 0; i < params.length; i++) {
            const temp = params[i];
            
            string.replace(new RegExp(`{${i}}`, 'g'), temp);
        }

        return str;
    }
}
solve();

let str = 'my string';
str = str.ensureStart('my');
console.log(str);

str = str.ensureStart('hello ');
console.log(str);

str = str.truncate(16);
console.log(str);

str = str.truncate(14);
console.log(str);

str = str.truncate(8);
console.log(str);

str = str.truncate(4);
console.log(str);

str = str.truncate(2);
console.log(str);

str = String.format('The {0} {1} fox',
  'quick', 'brown');
console.log(str);

str = String.format('jumps {0} {1}',
  'dog');
console.log(str);


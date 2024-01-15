export default class Pricing {
    constructor(amount, currency) {
      if (typeof amount !== 'number') throw TypeError('Amount must be a number');
      this._amount = amount;
      this._currency = currency;
    }
  
    // Getter
  
    get amaunt() {
      return this._amount;
    }
  
    get currency() {
      return this._currency;
    }
  
    // Setters
  
    setAmount(newAmount) {
      if (typeof newAmount !== 'number') throw TypeError('Amount must be a number');
      this._amount = newAmount;
    }
  
    setCurrency(newCurrency) {
      this._amount = newCurrency;
    }
  
    displayFullPrice() {
      return `${this.amaunt} ${this.currency.name} (${this.currency.code})`;
    }
  
    static convertPrice(amauntToConvert, conversionRate) {
      return amauntToConvert * conversionRate;
    }
}

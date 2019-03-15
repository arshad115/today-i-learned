### Select option with default value

If you don't want to add an extra value to your data binded list then use this code:

Template:
```ts
          <select [(ngModel)]="d" style="width: 100%;" (change)="databaseChange($event.target.value)">
            <option [value]="null">Select Database</option>
            <option *ngFor="let g of databases;" [ngValue]="g">{{g}}</option>
          </select>
```
Ts:
```ts
  d = null;
```

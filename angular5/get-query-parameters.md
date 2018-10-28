# Get query parameters

If you want to get the query parameters:

```js
import {ActivatedRoute} from '@angular/router';
...

constructor(private route:ActivatedRoute){}
bankName:string;

ngOnInit(){
    // 'bank' is the name of the route parameter
    this.bankName = this.route.snapshot.params['bank'];
}
```

 Solution found here: https://stackoverflow.com/questions/40275862/how-to-get-parameter-on-angular2-route-in-angular-way
### Send multipart form data with post request

Below is the code to send a request with multipart/form-data in Angular 7.

```
  uploadData(data) {
    const headers = new HttpHeaders();
    headers.append('Content-Type', 'application/json');
    const requestOptions = {
      headers: headers
    };

    return this.httpClient.post(this.apiUrl, data, requestOptions).toPromise();
  }
```

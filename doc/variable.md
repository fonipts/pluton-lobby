# Variable syntax

## Sample syntax

In a browser :
```html
{{choices.database}}

==
{{name}}

==
{{name|ucfirst}}
==
{{name|replace(e,1)}}
==
{{name|if(dev,1)}}

```

### Action you can use in variable syntax

|Action type | Description | Example| Status |
|------------- | ------------- |------------- |------------- |
|ucfirst | Upper case first string | {{name|ucfirst}} | Dev |
|lower | Lower case string | {{name|lower}}| Dev |
|upper | Upper case string | {{name|upper}}| Dev |
|replace | Replace string | {{name|replace(e,1)}}| Dev |
|if | If statement string | {{name|if(dev,1)}} | Dev |

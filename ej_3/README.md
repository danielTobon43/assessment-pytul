## Dependencies
```
pip install -r requirements.txt
```

## Usage
```python
python3 main.py
```

## Configuration file: config.ini
File to set matrix size, start and target point.
```ini
[DEFAULT]
size = 10
start = 0, 0
goal = 2, 3
```

## Example
```python
➜ python3 example.py                    

- input matrix: 
[[1 1 1 1 1 1 1 1 1 1]
 [1 1 1 1 1 1 1 1 1 1]
 [1 1 1 1 1 1 1 1 1 1]
 [1 1 1 1 1 1 1 1 1 1]
 [1 1 1 1 1 1 1 1 1 1]
 [1 1 1 1 1 1 1 1 1 1]
 [1 1 1 1 1 1 1 1 1 1]
 [1 1 1 1 1 1 1 1 1 1]
 [1 1 1 1 1 1 1 1 1 1]
 [1 1 1 1 1 1 1 1 1 1]]

- shortest path: [(1, 0), (2, 0), (2, 1), (2, 2)]
- cost: 4

```
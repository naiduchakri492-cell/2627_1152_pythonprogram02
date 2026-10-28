Here is your complete project for SUM OF DIGITS:
1. PROBLEM STATEMENT
To write a Python program to find the sum of digits of a given number using loop.
Example: If number is 123 -> 1+2+3 = 6
2. ALGORITHMjavascript1. Start
2. Input num
3. Set sum = 0
4. While num > 0:
      a. digit = num % 10 (get last digit)
      b. sum = sum + digit
      c. num = num // 10 (remove last digit)
5. Print sum
6. Stop3. FLOWCHART
START -> INPUT num -> sum=0 -> num>0? -> YES -> digit=num%10 -> sum=sum+digit -> num=num//10 -> LOOP -> NO -> PRINT sum -> END
7. MERMAID FLOWCHART CODE
Paste this in https://mermaid.live/mermaidflowchart TD
    A([START]) --> B[/Input num/]
    B --> C[sum = 0]
    C --> D{num > 0?}
    D -->|Yes| E[digit = num % 10]
    E --> F[sum = sum + digit]
    F --> G[num = num // 10]
    G --> D
    D -->|No| H[/Print sum/]
    H --> I([END])

    style A fill:#b3e5fc,stroke:#0288d1
    style H fill:#c8e6c9,stroke:#388e3c
    style I fill:#b2dfdb,stroke:#00796b

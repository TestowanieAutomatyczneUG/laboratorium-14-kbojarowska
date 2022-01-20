Feature: Book

    @book @en
    Scenario Outline: Create book
        Given book title <title>
        And book author Tomasz, Karolak, t.karolak@gmail.com
        And book isbn <isbn>
        When creating book
        Then book is <result>

        Examples:
            | title     | isbn                             | result        |
            | Biografia | 978-3-16-148410-0                | created        |
            | Ksiazka1  | 9783161484100                    | created        |
            | Ksiazka2  | 9-7-8-0-1-3-6-0-9-1-8-1-3        | created        |
            | Ksiazka3  | 0000000000000000000000000000000  | not created    |
            | Ksiazka4  | 0000000000001                    | not created    |
            | Ksiazka5  | ''                               | not created    |

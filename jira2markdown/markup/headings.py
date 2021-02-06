from pyparsing import Combine, LineStart, ParseResults, ParserElement, Word


class Headings:
    def action(self, tokens: ParseResults) -> str:
        return "#" * int(tokens[0][1]) + " "

    @property
    def expr(self) -> ParserElement:
        return LineStart() + Combine(Word("h", "123456", exact=2) + ". ").setParseAction(self.action)
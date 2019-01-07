import re
def removeComments(source):
	pattern = '\/\/.*|\/\*(.|\n)*?\*\/'
	s = "\n".join(source)
	s = re.sub(pattern, '', s)
	return [el for el in s.split("\n") if el]

	# return  list(filter(None, re.sub('//.*|/\*(.|\n)*?\*/', '', '\n'.join(source)).split('\n')))

print(removeComments(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))


print(removeComments(["main() {", "   int x = 1; // Its comments here", "   x++;", "   cout << x;", "   //return x;", "   x--;", "}"]))

print(removeComments(["main() {", "/* here is commments", "  // still comments */", "   double s = 33;", "   cout << s;", "}"]))



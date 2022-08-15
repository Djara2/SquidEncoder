#include <stdlib.h>
#include <string>
int main()
{
	std::string scmd = "python squidencoder.py";
	const char* cmd = scmd.c_str();
	system(cmd);
	return 0;
}

dc3d.so : dc3d_wrapper.o DC3D.o
	gcc -shared -o $@ $< DC3D.o -lgfortran
dc3d_wrapper.o : dc3d_wrapper.c
	gcc -Wall -fPIC -c $<
DC3D.o: DC3D.f
	gcc -Wall -fPIC -c $< -lgfortran
install:
	make
	cp dc3d.so /usr/lib/
uninstall:
	rm /usr/lib/dc3d.so
clean:
	rm *.o *.so

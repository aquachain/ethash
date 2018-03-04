.PHONY: clean test
test:
	./test/test.sh

clean:
	rm -rf *.so pyaquahash.egg-info/ build/ test/python/python-virtual-env/ test/c/build/ pyaquahash.so test/python/*.pyc dist/ MANIFEST

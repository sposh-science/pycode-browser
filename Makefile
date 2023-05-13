DESTDIR=
SHAREDIR=/usr/share/pycode-browser
BINDIR=$(DESTDIR)/usr/bin
APPDIR=$(DESTDIR)/usr/share/applications

all:
	make -C pybooksrc all DESTDIR=$(DESTDIR)

clean:
	rm -f *~
	make -C pybooksrc clean

install:
	mkdir -p $(DESTDIR)$(SHAREDIR)
	cp -a Code gui pycode-browser.py $(DESTDIR)$(SHAREDIR)
	cp pybooksrc/mapy.pdf $(DESTDIR)$(SHAREDIR)/
	find $(DESTDIR)$(SHAREDIR) -type f -exec chmod 466 {} \;
	mkdir $(BINDIR)
	echo "#! /bin/sh" > $(BINDIR)/pycode-browser
	echo "python $(SHAREDIR)/pycode-browser.py" >> $(BINDIR)/pycode-browser
	echo "#! /bin/sh" > $(BINDIR)/pycode-browser-book
	echo "evince $(SHAREDIR)/mapy.pdf" >> $(BINDIR)/pycode-browser-book
	mkdir -p $(APPDIR)
	install -m 644 *.desktop $(APPDIR)




SPHINXOPTS  ?=
SPHINXBUILD ?= sphinx-build
SOURCEDIR   = .
BUILDDIR    = _build
AUTODOCDIR  = api

ifeq ($(shell which $(SPHINXBUILD) > /dev/null 2>&1; echo $?), 1)
$(error "The '$(SPHINXBUILD)' command was not found. Make sure that sphinx is installed, and then ensure that the proper environment variables are set")
endif

.PHONY: help clean the Makefile

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean:
	rm -rf $(BUILDDIR)/* $(AUTODOCDIR)

%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" "$(SPHINXOPTS)" $(O)
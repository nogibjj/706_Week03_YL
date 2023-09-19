install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

test:
	python -m pytest -vv --cov=descriptive test_*.py

add_commit_push:
    @if [ -n "$$(git status --porcelain)"]; then \
	        git config --local user.email "action@github.com"; \
	        git config --local user.name "GitHub Action"; \
	        git add figures/points-hist.png figures/scatter.png report.md; \
	        git commit -m "Add generated visualization"; \
	        git push; \
	else \
	        echo "No changes to commit. Skipping commit and push."; \
	fi

update_readme:
        cat report.md >> README.md
		git add README.md
		git commit -m "merge readmes"
		git push   
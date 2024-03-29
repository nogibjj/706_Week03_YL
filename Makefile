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
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add pairplot.png boxplots.png Statistics_report.md; \
		git commit -m "Add generated plot image"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi


update_readme:
	cat Statistics_report.md >> README.md
	git add README.md
	git commit -m "merge readmes"
	git push  
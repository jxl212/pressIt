from flask import Flask, render_template, flash, redirect,url_for

from pressItApp import app
from pressItApp.crawler import Crawler
from pressItApp.scraper import Scraper
from pressItApp.forms import LoginForm, CrawlForm


@app.route('/')
def do_crawling():
	return redirect(url_for('init_crawlling'))


@app.route('/init', methods=['GET', 'POST'])
def init_crawlling():

	form = CrawlForm()
	if form.validate_on_submit():
		flash('Crawl requested: {}/{}'.format(form.ip_address.data, form.ip_range.data))
		urls = Crawler.start_crawling(form.ip_address.data,form.ip_range.data)
		ret_str=""
		wp_urls = []
		other_urls = []

		for url in urls:
			if Scraper.wordpress_login_exists(url):
				wp_urls.append(url)
			else:
				other_urls.append(url)
		
		return render_template('base.html', title='PressIt', wp_urls=wp_urls, other_urls=other_urls)
	return render_template('init.html', title='PressIt', form=form)




import tkinter as tk
from newspaper import article
import urllib.request
import requests
from newspaper import Article
from tkinter import messagebox
import sys


class myApp:
	def __init__ (self, master):

		self.url_label = tk.Label(master, text="ENTER URL OF THE ARTCLE")
		self.url_label.grid(row=0, column=0, padx=10, pady=10)

		self.url_entry = tk.Entry(master, width=75)
		self.url_entry.grid(row=0, column=1, padx=10, pady=10)

		self.name_lable = tk.Label(master, text="SAVE AS")
		self.name_lable.grid(row=1, column=0, padx=10, pady=10)

		self.name_entry = tk.Entry(master, width=75)
		self.name_entry.grid(row=1, column=1, padx=10, pady=10)

		self.submit_button = tk.Button(master, text="SUBMIT!", command=self.saveArticle)
		self.submit_button.grid(row=2,column=0, columnspan=2, padx=10, pady=10)



	def saveArticle(self):
		URL = self.url_entry.get()
		NAME = self.name_entry.get() + ".txt"

		try:
			content = self.parse_article(URL)

		except:
			messagebox.showinfo(title="error", message="ARTICLE CANNOT BE SAVED DUE TO SITE RESTRICTIONS!")
			sys.exit(0)


		file = open(NAME, "w")
		file.write(content)
		file.close()

		messagebox.showinfo(title="SUCCESS!", message="ARTICLE SAVED SUCCESSFULLY!")



	def parse_article(self, url) -> str:
		article = Article(url, language="en")
		article.download()
		article.parse()
		# article.nlp()

		return article.text
		


root = tk.Tk()
root.title("Article Grabber")
root.config()
root.resizable(False, False)


app = myApp(root)


root.mainloop()

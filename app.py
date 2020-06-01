#!/usr/bin/env python

import os
import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns

def main():
	st.title("Temperature Data Explorer :thermometer:")
	st.subheader("Datasets for temperatures in cities")


	def file_selector(folder_path='./datasets'):
		filenames = os.listdir(folder_path)
		if st.button("Alphabetical Order"):
			filenames.sort()
			st.write(filenames)
		if st.button("Reverse Alphabetical Order"):
			reverseNames =  sorted(filenames, reverse=True)
			st.write(reverseNames)
		selected_filename = st.selectbox("Select A file",filenames,key="na_upper")
		return os.path.join(folder_path,selected_filename)

	def file_selector2(folder_path='./datasets'):
		filenames = os.listdir(folder_path)
		selected_filename = st.selectbox("Select A file",filenames,key="na_lower")
		return os.path.join(folder_path,selected_filename)

	filename = file_selector()
	st.info("You Selected {}".format(filename))

	# This code reads the dataset selected by the user
	df = pd.read_csv(filename)



	def get_data(filename,keyID):
		if st.checkbox("Show Dataset",key=keyID):
			raw_folder_path='./rawData'
			rawFiles = os.listdir(raw_folder_path)
			raw_df = pd.read_csv(filename)
			if ("Boston" in filename):
				raw_df = pd.read_csv('./rawData/dataexport_20200529T213040.csv')
			elif ("Miami" in filename):
				raw_df = pd.read_csv('./rawData/dataexport_20200529T213325.csv')
			elif ("Vegas" in filename):
				raw_df = pd.read_csv('./rawData/dataexport_20200529T213304.csv')
			elif ("Minneapolis" in filename):
				raw_df = pd.read_csv('./rawData/dataexport_20200529T213252.csv')
			elif ("Angeles" in filename):
				raw_df = pd.read_csv('./rawData/dataexport_20200529T213229.csv')
			elif ("Seattle" in filename):
				raw_df = pd.read_csv('./rawData/dataexport_20200529T213211.csv')
			elif ("Philadelphia" in filename):
				raw_df = pd.read_csv('./rawData/dataexport_20200529T213151.csv')
			elif ("Washington" in filename):
				raw_df = pd.read_csv('./rawData/dataexport_20200529T213133.csv')
			elif ("Houston" in filename):
				raw_df = pd.read_csv('./rawData/dataexport_20200529T213110.csv')
			elif ("Boston" in filename):
				raw_df = pd.read_csv('./rawData/dataexport_20200529T213040.csv')
			elif ("York" in filename):
				raw_df = pd.read_csv('./rawData/dataexport_20200529T213019.csv')
			elif ("Chicago" in filename):
				raw_df = pd.read_csv('./rawData/dataexport_20200529T212951.csv')
			elif ("Antonio" in filename):
				raw_df = pd.read_csv('./rawData/dataexport_20200529T212901.csv')
			elif ("Diego" in filename):
				raw_df = pd.read_csv('./rawData/dataexport_20200529T212845.csv')
			elif ("Francisco" in filename):
				raw_df = pd.read_csv('./rawData/dataexport_20200529T212809.csv')
			st.dataframe(raw_df)


	get_data(filename,"1")

	if st.checkbox("Summary"):
		st.write(df.describe().T)


	st.subheader("Data Visualization")


	# This code shows a pie chart
	if st.checkbox("Pie Plot"):
		all_columns_names = df.columns.tolist()
		if st.button("Generate Pie Plot",key="3"):
			st.success("Generating A Pie Plot")
			st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
			st.pyplot()

	if st.checkbox("Plot of Value Counts"):
		st.text("Value Counts By Target")
		all_columns_names = df.columns.tolist()
		primary_col = st.selectbox("Primary Columm to GroupBy",all_columns_names)
		selected_columns_names = st.multiselect("Select Columns",all_columns_names)
		if st.button("Plot"):
			st.text("Generate Plot")
			if selected_columns_names:
				vc_plot = df.groupby(primary_col)[selected_columns_names].count()
			else:
				vc_plot = df.iloc[:,-1].value_counts()
			st.write(vc_plot.plot(kind="bar"))
			st.pyplot()


	st.subheader("Customizable Plot")

	all_columns_names = df.columns.tolist()
	type_of_plot = st.selectbox("Select Type of Plot",["area","bar","line","hist","box","kde"])
	selected_columns_names = st.multiselect("Select Columns To Plot",all_columns_names)


	if st.button("Generate Plot"):
		st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))

		if type_of_plot == 'area':
			cust_data = df[selected_columns_names]
			st.area_chart(cust_data)

		elif type_of_plot == 'bar':
			cust_data = df[selected_columns_names]
			st.bar_chart(cust_data)

		elif type_of_plot == 'line':
			cust_data = df[selected_columns_names]
			st.line_chart(cust_data)

		elif type_of_plot:
			cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
			st.write(cust_plot)
			st.pyplot()



	st.sidebar.header("About")
	st.sidebar.text("Built with Streamlit")
	st.sidebar.text("Made by Anish Thiriveedhi")


if __name__ == '__main__':
	main()

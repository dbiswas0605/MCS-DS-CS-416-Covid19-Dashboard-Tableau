# merge the columns
import pandas as pd
import os

rawdatasetpath = "F:/OneDrive/MCS-DS/CS 416 Data Visualization (Summer 2021)/Week 4/MCS-DS-CS-416-Covid19-Dashboard-Tableau/Covid 19 Data/Test"
cleandatasetpath = "F:/OneDrive/MCS-DS/CS 416 Data Visualization (Summer 2021)/Week 4/MCS-DS-CS-416-Covid19-Dashboard-Tableau/Covid 19 Data/Clean_dataset"


def removefiledescription(fname):
    fn = rawdatasetpath + '/' + fname
    f = open(fn)
    output = []

    for line in f:
        if line.__contains__(','):
            output.append(line)
    f.close()
    f = open(fn, 'w')
    f.writelines(output)
    f.close()


def mergecolumns(fname1, fname2, colname, outfile):
    data1 = pd.read_csv(rawdatasetpath + '/' + fname1)
    data2 = pd.read_csv(rawdatasetpath + '/' + fname2)

    data1.pop('Percent of US population')
    data2.pop('Percent of US population')

    output1 = pd.merge(data1, data2,
                       on=colname,
                       how='inner')

    output1.to_csv(cleandatasetpath + '/' + outfile)


# remove file description
removefiledescription('cases_by_race_ethnicity__all_age_groups.csv')
removefiledescription('deaths_by_race_ethnicity__all_age_groups.csv')

removefiledescription('cases_by_age_group.csv')
removefiledescription('deaths_by_age_group.csv')

removefiledescription('cases_by_sex__all_age_groups.csv')
removefiledescription('deaths_by_sex__all_age_groups.csv')

# merge-columns
mergecolumns('cases_by_race_ethnicity__all_age_groups.csv','deaths_by_race_ethnicity__all_age_groups.csv','Race/Ethnicity','cases by race.csv')
mergecolumns('cases_by_age_group.csv','deaths_by_age_group.csv','Age Group','cases by age group.csv')
mergecolumns('cases_by_sex__all_age_groups.csv','deaths_by_sex__all_age_groups.csv','Sex','cases by sex.csv')

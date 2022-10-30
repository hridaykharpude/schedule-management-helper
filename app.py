#Import libraries
import gradio as gr
import numpy as np
import pandas as pd

#Assembling and Processing Data
def prepData(engSL,engHL,
             hindiBSL,hindiBHL,
             spanAbSL,spanAbHL,spanBSL,spanBHL,
             frenchAbSL,frenchAbHL,frenchBSL,frenchBHL,
             bmSL,bmHL,econSL,econHL,
             psychSL,psychHL,
             chemSL,chemHL,bioSL,bioHL,
             phySL,phyHL,csSL,csHL,
             maaSL,maaHL,maiSL,maiHL,
             vaSL,vaHL,
             essSL,essHL):
    data = [engSL,engHL,
             hindiBSL,hindiBHL,
             spanAbSL,spanAbHL,spanBSL,spanBHL,
             frenchAbSL,frenchAbHL,frenchBSL,frenchBHL,
             bmSL,bmHL,econSL,econHL,
             psychSL,psychHL,
             chemSL,chemHL,bioSL,bioHL,
             phySL,phyHL,csSL,csHL,
             maaSL,maaHL,maiSL,maiHL,
             vaSL,vaHL,
             essSL,essHL]
    
    #Location for assmebling all subjects data
    subsData = []
    subs = "engSL engHL hindiBSL hindiBHL spanAbSL spanAbHL spanBSL spanBHL frenchAbSL frenchAbHL frenchBSL frenchBHL bmSL bmHL econSL econHL psychSL psychHL chemSL chemHL bioSL bioHL phySL phyHL csSL csHL maaSL maaHL maiSL maiHL vaSL vaHL essSL essHL"
    subs = subs.split()
    for i in range(len(subs)):
        subsData.append([subs[i]])
    
    #Counters
    k = -1
    count = 0
    
    for i in range(len(data)):
        #Inside each subject
        k = k+1
        #print(i,k)
        lst=data[i].split()
        for j in lst:
            #print(k,j)            
            subsData[k].append(j)
            
        if len(lst)==0:
            #print("entered")
            subsData.remove(subsData[k])
            k = k-1
    
    
    #Processing Data        
    compensations = []
    for sub1 in range(k):
        #compensations = []
    
        for sub2 in range(sub1+1, k+1):
            #print(temp[sub1][0],temp[sub2][0])
            compensations.append([subsData[sub1][0]+"/"+subsData[sub2][0]])
            #compensations.append(list('/'.join(compensations[count])))
            cmn_lst = []
        
            for i in range(1,len(subsData[sub1])):
            
                for j in range(1,len(subsData[sub2])):
                
                    if subsData[sub1][i] == subsData[sub2][j]:
                        cmn_lst.append(subsData[sub2][j])
                        #print(temp[sub2][j])
        
            compensations[count].append(len(cmn_lst))
            cmn_lst = ' '.join(cmn_lst)
            compensations[count].append(cmn_lst)
            count=count+1
            #print(compensations)

    for i in range(len(compensations)):
        for j in range(len(compensations[0])):
            #print(compensations[i][j])
            if compensations[i][j] == 0:
                compensations[i][j+1]="NONE"
           
    print(pd.DataFrame(compensations))
            

    #print(pd.DataFrame(subsData).head())
    return compensations



def sortData(btnVal,compensation):

    compensations = compensation.values.tolist()
    print(type(compensations))
    print(compensations[1][1])
    
    
    if btnVal == "All":
        return compensations
    if btnVal == "Max 3":
        count = -1
        three = compensations
        for rowNo in range(len(three)):
            count = count + 1
            if three[count][1] > 3:
                three.remove(three[count])
                count = count - 1
        return three
    if btnVal == "Max 2":
        count = -1
        two = compensations
        for rowNo in range(len(two)):
            count = count + 1
            if two[count][1] > 2:
                two.remove(two[count])
                count = count - 1
        return two
    if btnVal == "Max 1":
        count = -1
        one = compensations
        for rowNo in range(len(one)):
            count = count + 1
            if one[count][1] > 1:
                one.remove(one[count])
                count = count - 1
        return one
    if btnVal == "No Compensations":
        count = -1
        none = compensations
        for rowNo in range(len(none)):
            count = count + 1
            if none[count][1] > 0:
                none.remove(none[count])
                count = count - 1
        return none



with gr.Blocks() as heart:
        
    gr.HTML("<div style='font-size: 35px; font-family: Georgia; color: black; text-align: center'>Schedule Management Helper</div>")
    
    #Entry fields are here
    inpSubsData = []
    gr.HTML("<div style='font-size: 20px; font-family: Georgia; color: black'>Group I - English Language and Literature</div>")
    with gr.Column():
        with gr.Row():
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for ENGLISH SL")) #1
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for ENGLISH HL")) #2
    
    gr.HTML("<div style='font-size: 20px; font-family: Georgia; color: black'>Group II - Language Acquisition- Hindi B, Spanish, French</div>")
    with gr.Column():
        with gr.Row():
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for HINDI B SL")) #3
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for HINDI B HL")) #4
        with gr.Row():
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for SPANISH AB INITIO SL")) #5
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for SPANISH AB INITIO HL")) #6
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for SPANISH B SL")) #7
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for SPANISH B HL")) #8
        with gr.Row():            
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for FRENCH AB INITIO SL")) #9
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for FRENCH AB INITIO HL")) #10
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for FRENCH B SL")) #11
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for FRENCH B HL")) #12
    
    gr.HTML("<div style='font-size: 20px; font-family: Georgia; color: black'>Group III - Business Management, Economics, Psychology</div>")
    with gr.Column():
        with gr.Row():
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for BM SL")) #13
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for BM HL")) #14
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for ECON SL")) #15
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for ECON HL")) #16
        with gr.Row():
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for PSYCH SL")) #17
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for PSYCH HL")) #18
          
    gr.HTML("<div style='font-size: 20px; font-family: Georgia; color: black'>Group IV - Chemistry, Biology, Physics, Computer Science</div>")
    with gr.Column():
        with gr.Row():
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for CHEM SL")) #19
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for CHEM HL")) #20
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for BIO SL")) #21
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for BIO HL")) #22
        with gr.Row():            
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for PHYSICS SL")) #23
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for PHYSICS HL")) #24
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for CS SL")) #25
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for CS HL")) #26
    
    gr.HTML("<div style='font-size: 20px; font-family: Georgia; color: black'>Group V - Mathematics Analysis and Approaches and Mathematics Application and Interpretation</div>")
    with gr.Column():
        with gr.Row():
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for MAA SL")) #27
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for MAA HL")) #28
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for MAI SL")) #29
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for MAI HL")) #30
   
    with gr.Row():
        with gr.Column():            
            gr.HTML("<div style='font-size: 20px; font-family: Georgia; color: black'>Group VI - Arts- Visual arts</div>")
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for VA SL")) #31
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for VA HL")) #32
        with gr.Column():
            gr.HTML("<div style='font-size: 20px; font-family: Georgia; color: black'>Group III & IV - Environmental Societies and Systems</div>")
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for ESS SL")) #33
            inpSubsData.append(gr.Textbox(placeholder="Enter student list here",label="Student List for ESS HL")) #34
            
    sbmt_btn = gr.Button("Accept Data").style(full_width=True)
    
    sort_btn = gr.Radio(["All","Max 3","Max 2","Max 1","No Compensations"],value='None', show_label=False)
    
    #Output is here
    out=gr.Dataframe(headers=["Parallel Subjects","No. of Compensations","Compensations"])
    
    #Button Functions
    sbmt_btn.click(prepData, inpSubsData, out)
    sort_btn.change(sortData, inputs=[sort_btn, out], outputs=out)

heart.launch(share=True)

# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
# Reference for writing methog - https://github.com/tensorflow/tensorflow/blob/v2.1.0/tensorflow/python/keras/optimizer_v2/rmsprop.py#L63-L119
import re
import inspect
import os.path
import subprocess
import sys

class crystal_ball:
    def __init__(self, *sample_size, *learning_rate, *epochs, *batch_size, **kwargs):
        # * is for args; args will give us all the function parameters in the form of a list
        # Get filename from calling file
        """
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        """
        method_list=['grid_search','bayesian_search']
        # make the path absolute (optional)
        # get the caller's stack frame and extract its file path
        frame_info = inspect.stack()[1]
        filepath = frame_info.filename  # This is for python 3.5+, for earlier versions you can use frame_info[1]
        del frame_info  # drop the reference to the stack frame to avoid reference cycles
        filepath_full = os.path.abspath(filepath)

        self._sample_size=sample_size
        self._learning_rate=learning_rate
        self._epochs=epochs
        self._batch_size=batch_size
        #Copy full file content into a seperate
        with open("filepath","r") as myfile:
            filetext=myfile.read() # myfile.readlines() on the other hand will each lines in one string each

        # Search & delete from filetext of calling file the calling method lines completely i.e. remove grid_search, bayesian_search etc.
        for a in filetext: # Iterate across entire file lines
            for b in method_list: # Iterate across methods under crystal ball to remove from file text
                if(b in a):
                    filetext.remove(a)
                    insert_index=filetext.index(a) # This is where to insert loop code

        # Re-write the file with the crystal_ball method lines removed
        with open(filepath_full,'w') as myfile1:
            myfile1.writelines(filetext)

        # Command-line entry format learning_rate, epochs, batch_size
        #Now lets add line which allows all variables to be entered as command line n_inputs
        #argumentList = sys.argv
        """
        new_add_ln_file=
        ["
        file_name = sys.argv[0] # Print the name of file
        learning_rate = sys.argv[1] # Print the first argument after the name of file i.e. learning_rate
        epochs = sys.argv[2] # Print the second argument after the name of file i.e. epochs
        batch_size = sys.argv[3] # Print the second argument after the name of file i.e. batch_size
        "]

        #Create a copy of the file w/o crystal_ball lines
        with open('temp.py', 'w') as newfile:
            for line in filetext:
                if (line.find("crystal_ball") == -1):
                    newfile.write(line)
                else:
                    print("Ignoring calling function in copy to avoid calling function calling itself repeatedly")
        """
        #We will also write a line to record all outputs in a separate file

        #completed = subprocess.run([filepath, 'cmd_ln_arg_1','cmd_ln_arg_2'...])
        completed = subprocess.run(argumentList)
        print('returncode:', completed.returncode)

        #Refer to full set of algos - https://medium.com/criteo-labs/hyper-parameter-optimization-algorithms-2fe447525903  https://towardsdatascience.com/hyperparameter-tuning-c5619e7e6624
        # Exhaustive search
        #   Grid Search
        #   Random search
        # Surrogate model
        #   Bayesian Optimization
        #   Tree-structured Parzen estimators
        # Algos for Hyperparameter tuning
        #   Hyperband
        #   PBT (Population-based training)
        #   Fabolas
        #   BOHB
        # Copy file in a string and then Search


    def grid_search(self):
        filetext.insert("for learning_rate,epochs in zip(learning_rate,epochs):",insert_index) # Insert looping line
        # Increasing indent for all subsequent lines of code
        count=0
        for a in filetext:
            if count>insert_index:
                filetext1.append("    "+a)
            else:
                filetext1.append(a)
            count+=1

        wevwve
        run self file with self.sample_size=a, self.learning_rate=b, self.epochs=c, for a in self.sample_size for b in self.learning_rate

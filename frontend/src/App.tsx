import React from "react";
import "./App.css";
import {
  Box,
  Center,
  Heading,
  Tabs,
  TabList,
  TabPanels,
  Tab,
  TabPanel,
  Text,
} from "@chakra-ui/react";
import MostCitedPapers from "./components/MostCitedPapers";
import MostRelatedInsitutions from "./components/MostRelatedInsitutions";

function App() {
  return (
    <div className="App">
      <Heading mt={4}>Education Today</Heading>
      <Text align="center">by Kuan-Yin Chen (kuanyin2)</Text>
      <Center>
        <Box w="100%" maxW="1024px" mt={4}>
          <Tabs>
            <TabList>
              <Tab>Task 1: Most Cited Paper</Tab>
              <Tab>Task 2: Most Related Insitutions</Tab>
            </TabList>

            <TabPanels>
              <TabPanel>
                <MostCitedPapers />
              </TabPanel>
              <TabPanel>
                <MostRelatedInsitutions />
              </TabPanel>
            </TabPanels>
          </Tabs>
        </Box>
      </Center>
    </div>
  );
}

export default App;

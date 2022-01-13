import React from "react";
import "./App.css";
import { VStack, StackDivider, Box, Center, Heading } from "@chakra-ui/react";
import MostCitedPapers from "./components/MostCitedPapers";

function App() {
  return (
    <div className="App">
      <Center>
        <Box w="100%" maxW="1024px">
          <VStack
            divider={<StackDivider borderColor="gray.200" />}
            spacing={4}
            align="stretch"
            p={4}
          >
            <Heading>Education Today</Heading>
            <MostCitedPapers />
          </VStack>
        </Box>
      </Center>
    </div>
  );
}

export default App;

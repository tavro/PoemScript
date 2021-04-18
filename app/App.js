import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Text>PoemScript</Text>

      <View style={editorStyles.container}>
        <Button title="Compile" onPress={() => console.log("compiling...")}/>
      </View>

      <View style={editorStyles.container}>
        <Button title="Download" onPress={() => console.log("downloading...")}/>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
});

const editorStyles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#aaa',
    width: '50%',
  },
});